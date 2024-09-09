import { mount } from '@vue/test-utils';
import { describe, it, expect } from 'vitest';
import App from '@/App.vue';

describe('App.vue', () => {
  it('renders the correct initial message', () => {
    const wrapper = mount(App);
    expect(wrapper.find('h2').text()).toBe('Hello World!');
  });

  it('updates the message when input changes', async () => {
    const wrapper = mount(App);
    const input = wrapper.find('input');

    // Change the input value
    await input.setValue('Vitest is awesome!');

    // Check if the message updates
    expect(wrapper.find('h2').text()).toBe('Vitest is awesome!');
  });
});
