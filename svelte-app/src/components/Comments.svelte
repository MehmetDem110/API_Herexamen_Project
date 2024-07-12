<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  // Define writable store for comments data
  let commentsData = writable([]);

  onMount(async () => {
    try {
      const response = await fetch('http://localhost:8111/comments/?skip=0&limit=10');
      if (!response.ok) {
        throw new Error('Failed to fetch comments');
      }
      const data = await response.json();
      commentsData.set(data); // Set fetched data to the store
    } catch (error) {
      console.error('Error fetching comments:', error);
    }
  });
</script>
<h3><span>GET:</span> /comments/ </h3>
<div>
  <!-- Display comments list -->
  {#if $commentsData.length > 0}
    <ul>
      {#each $commentsData as comment}
        <li>
          <p><strong>Comments:</strong>{comment.text}</p>
          <p><strong>ID:</strong> {comment.id}</p>
          <p><strong>Post ID:</strong> {comment.post_id}</p>
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
    padding: 10px;
    display: flex;
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
