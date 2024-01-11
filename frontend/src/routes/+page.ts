import type { PageLoad } from './$types';

export const ssr = false;

export const load: PageLoad = async ({ fetch }) => {
	const res = await fetch(`/api/v1/quotes/`);
	const item = await res.json();

	console.log(item);

	return item;
};
