<script>
  import { writable } from 'svelte/store';

  // Define writable store for user data
  let userData = writable({});
  let userId = writable('');

  async function fetchUserData(event) {
    event.preventDefault();
    try {
      const response = await fetch(`http://localhost:8111/users/${$userId}`);
      if (!response.ok) {
        throw new Error('Failed to fetch user data');
      }
      const data = await response.json();
      userData.set(data); // Set fetched data to the store
    } catch (error) {
      console.error('Error fetching user data:', error);
    }
  }
</script>

<div>
  <h3>GET: /users/(user_id)</h3>
  <form on:submit={fetchUserData} class="form-container">
    <label>
      User ID:
      <input type="number" bind:value={$userId} required />
    </label>
    <button type="submit">Fetch User Data</button>
  </form>

  <!-- Access data from writable store -->
  {#if $userData.username}

    <div class="response-container">
      <p><strong>Username:</strong> {$userData.username}</p>
      <p><strong>Email:</strong> {$userData.email}</p>
      <p><strong>ID:</strong> {$userData.id}</p>
    </div>
  {:else}
    <p>Loading...</p>
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
