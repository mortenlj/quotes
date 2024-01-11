<script lang="ts">
	import type {PageData} from './$types';

	export let data: PageData;
</script>

<figure>
	<blockquote class="blockquote">
		<p>{data.quote}</p>
	</blockquote>
	{#if data.dedication}
		<figcaption class="blockquote-footer">
			{data.dedication}
		</figcaption>
	{/if}
</figure>
