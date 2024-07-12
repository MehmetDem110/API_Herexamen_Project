<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  // Define writable store for form data and response
  let formData = {
    title: '',
    content: '',
    user_id: ''
  };
  let responseData = writable(null);

  async function handleSubmit(event) {
    event.preventDefault();

    try {
      const response = await fetch(`http://localhost:8111/posts/?user_id=${formData.user_id}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          title: formData.title,
          content: formData.content
        })
      });

      if (!response.ok) {
        throw new Error('Failed to create post');
      }

      // Since the server doesn't return user_id, set it from formData
      const data = await response.json();
      responseData.set({
        ...data,
        user_id: formData.user_id // Set user_id from form input
      });
    } catch (error) {
      console.error('Error creating post:', error);
    }
  }
</script>
<h3>POST: /posts/</h3>
<div>
  <form on:submit={handleSubmit} class="form-container">
    <label>
      User ID:
      <input type="number" bind:value={formData.user_id} required />
    </label>
    <label>
      Title:
      <input type="text" bind:value={formData.title} required />
    </label>
    <label>
      Content:
      <textarea bind:value={formData.content} required></textarea>
    </label>
    <button type="submit">Create Post</button>
  </form>

  <!-- Display response data -->
  {#if $responseData}
    <div class="response-container">
      <h2>Response:</h2>
      <p><strong>Title:</strong> {$responseData.title}</p>
      <p><strong>Content:</strong> {$responseData.content}</p>
      <p><strong>User ID:</strong> {$responseData.user_id}</p>
    </div>
  {/if}
</div>

<style>
  .form-container {
    display: flex;
    flex-direction: column;
    gap: 10px; /* Adds space between the form elements */
  }

  .form-container label {
    display: flex;
    flex-direction: column;
  }

  .response-container {
    display: flex;
    flex-direction: column;
    gap: 10px; /* Optional: Adds space between the items */
  }

  h3{
    width: 100%;
    border-bottom: 2px solid black;
    text-align: center;
  }
</style>
