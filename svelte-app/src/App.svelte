
<script>
  import Comments from './components/Comments.svelte';
  import User from './components/User.svelte';
  import Post from './components/Post.svelte';
  import CreateUser from "./components/CreateUser.svelte";
  import CreatePost from "./components/CreatePost.svelte";
  import CreateComment from "./components/CreateComment.svelte";
  import 'bootstrap/dist/css/bootstrap.min.css';
  import 'bootstrap'
</script>
<header>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</header>
<main>
    <h1>Frontend API Herexamen using Svelte</h1>
    <div class="text">
        <p>        Ik heb voor mijn frontend framework gebruik gemaakt van svelte en heb alle get en post endpoint er in gezet.</p>
    </div>
<div class="row">
    <div class="col-6">
        <h2 class="text-center">Alle Get endpoints</h2>
        <br><br><br>
      <div>
          <User />
      </div>
        <br><br><br>
      <div>
          <Post />
      </div>
        <br><br><br>
      <div>
          <Comments />
      </div>
    </div>

    <div class="col-6">
        <h2 class="text-center">Alle Post enpoints</h2>
        <br><br><br>
      <div>
          <CreateUser />
      </div>
        <br><br><br>
      <div>
          <CreatePost />
      </div>
        <br><br><br>
      <div>
          <CreateComment />
      </div>
    </div>
</div>


</main>
t
<style>

    h1{
        text-align: center;
        background: #ff8000;
        padding: 20px;
        font-size: 60px;
    }

    .text{
        text-align: center;
        padding: 80px 0 80px 0;
        background-color: #ffe5b0;
        font-size: 22px;
    }

    .row{
        background-color: #ececec;
    }

    .col-6 .text-center{
        margin: 30px 0 10px 0;
    }
</style>