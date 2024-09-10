import { mount } from '@vue/test-utils';
import { describe, it, expect } from 'vitest';
import App from '@/App.vue';

describe('App.vue', () => {
  it('renders the correct initial message', () => {
    const wrapper = mount(App);
    expect(wrapper.find('h1').text()).toBe('BuyHighSellLow.com');
  });
});
