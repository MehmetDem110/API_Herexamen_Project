<script>
  import { writable } from 'svelte/store';

  // Define writable store for form data and response
  let formData = {
    text: '',
    post_id: ''
  };
  let responseData = writable(null);

  async function handleSubmit(event) {
    event.preventDefault();

    try {
      const response = await fetch(`http://localhost:8111/comments/?post_id=${formData.post_id}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          text: formData.text
        })
      });

      if (!response.ok) {
        throw new Error('Failed to create comment');
      }

      // Since the server doesn't return post_id, set it from formData
      const data = await response.json();
      responseData.set({
        ...data,
        post_id: formData.post_id // Set post_id from form input
      });
    } catch (error) {
      console.error('Error creating comment:', error);
    }
  }
</script>
<h3>POST: /comments/</h3>
<div>
  <form on:submit={handleSubmit} class="form-container">
    <label>
      Post ID:
      <input type="number" bind:value={formData.post_id} required />
    </label>
    <label>
      Text:
      <textarea bind:value={formData.text} required></textarea>
    </label>
    <button type="submit">Create Comment</button>
  </form>

  <!-- Display response data -->
  {#if $responseData}
    <div class="response-container">
      <h2>Response:</h2>
      <p><strong>Text:</strong> {$responseData.text}</p>
      <p><strong>Post ID:</strong> {$responseData.post_id}</p>
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
