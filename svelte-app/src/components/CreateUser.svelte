<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  // Define writable store for form data and response
  let formData = {
    username: '',
    email: '',
    password: ''
  };
  let responseData = writable(null);

  async function handleSubmit(event) {
    event.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:8111/users/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });

      if (!response.ok) {
        throw new Error('Failed to create user');
      }

      const data = await response.json();
      responseData.set(data); // Set response data to the store
    } catch (error) {
      console.error('Error creating user:', error);
    }
  }
</script>

<h3>POST: /users/</h3>

<div>
  <form on:submit={handleSubmit} class="form-container">
    <label>
      Username:
      <input type="text" bind:value={formData.username} />
    </label>
    <label>
      Email:
      <input type="email" bind:value={formData.email} />
    </label>
    <label>
      Password:
      <input type="password" bind:value={formData.password} />
    </label>
    <button type="submit">Create User</button>
  </form>

  <!-- Display response data -->
  {#if $responseData}
    <div class="response-container">
      <h2>Response:</h2>
      <p><strong>Username:</strong> {$responseData.username}</p>
      <p><strong>Email:</strong> {$responseData.email}</p>
      <p><strong>ID:</strong> {$responseData.id}</p>
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
