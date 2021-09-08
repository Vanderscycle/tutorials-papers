import { writable } from 'svelte/store';
import type { Writable } from 'svelte/store'
export const messageStore: Writable<string[]> = writable(null);




