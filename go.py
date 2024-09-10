from gomatic import *

configurator = GoCdConfigurator(HostRestClient("localhost:8153"))

import os

git_token = os.getenv("GITHUB_TOKEN")

print(git_token)

pipeline = configurator \
    .ensure_pipeline_group("CD-Demo") \
    .ensure_replacement_of_pipeline("Continuous-Delivery") \
    .set_git_material(GitMaterial(f"https://{git_token}@github.com/oscols/DD2482-Demo.git", branch="dev", polling=False))

##### BUILD #####
build_stage = pipeline.ensure_stage("Build")
build_job = build_stage.ensure_job("Build")
build_job.add_task(ExecTask(['npm', 'install']))
build_job.add_task(ExecTask(['npm', 'run', 'build']))

##### TEST ######
test_stage = pipeline.ensure_stage("Test")
test_job = test_stage.ensure_job("Run-Tests")
test_job.add_task(ExecTask(['type', 'README.md']))

##### ACCEPTANCE TEST #####
acceptance_test_stage = pipeline.ensure_stage("AcceptanceTests")
acceptance_test_job = acceptance_test_stage.ensure_job("Run-Acceptance-Tests")
acceptance_test_job.add_task(ExecTask(['type', 'README.md']))

##### MOVE TO MAIN #####
deploy_to_staging_stage = pipeline.ensure_stage("Deploy-To-Staging")
deploy_to_staging_job = deploy_to_staging_stage.ensure_job("Merge-To-Main")
deploy_to_staging_job.add_task(ExecTask(['git', 'fetch', 'origin']))
deploy_to_staging_job.add_task(ExecTask(['git', 'checkout', 'main']))
deploy_to_staging_job.add_task(ExecTask(['git', 'pull', 'origin', 'main']))
deploy_to_staging_job.add_task(ExecTask(['git', 'merge', 'dev', '-m', 'Automatic merge of dev into main', '--no-ff']))
deploy_to_staging_job.add_task(ExecTask(['git', 'remote', '-v']))
deploy_to_staging_job.add_task(ExecTask(['git', 'push', 'origin', 'main']))