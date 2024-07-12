<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  // Define writable store for posts data
  let postData = writable([]);

  onMount(async () => {
    try {
      const response = await fetch('http://localhost:8111/posts/?skip=0&limit=10');
      if (!response.ok) {
        throw new Error('Failed to fetch posts');
      }
      const data = await response.json();
      postData.set(data); // Set fetched data to the store
    } catch (error) {
      console.error('Error fetching posts:', error);
    }
  });
</script>

<h3>GET: /posts/</h3>
<div>
  <!-- Display posts list -->
  {#if $postData.length > 0}
    <ul>
      {#each $postData as post}
        <li>
          <p><strong>title: </strong>{post.title}</p>
          <p><strong>content: </strong>{post.content}</p>
          <p><strong>ID: </strong> {post.id}</p>
          <p><strong>Owner ID: </strong> {post.owner_id}</p>
        </li>
      {/each}
    </ul>
  {:else}
    <p>Loading...</p>
  {/if}
</div>

<style>
  /* Optional: Your custom styles */
  ul {
    list-style-type: none;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
  }

  li {
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  h3{
    width: 100%;
    border-bottom: 2px solid black;
    text-align: center;
  }


</style>
