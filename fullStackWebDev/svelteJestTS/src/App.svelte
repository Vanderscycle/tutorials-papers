<script lang="ts">
    import Navbar from "./navbar.svelte"
    import Player from "./players.svelte"
    import AddPlayer from "./addPlayer.svelte"
    let players = [
        {
          name: "Bro McChad",
          points: 53
        },
        {
          name: "Sam Smith",
          points: 45
        },
        {
          name: "Sara Wilson",
          points: 34
        }
      ];
    const addPlayer = (e) => {
        const newPlayer = e.detail
        //console.log(newPlayer)
        players = [...players, newPlayer]
    }
</script>

<style>

</style>

<Navbar />
<main>
    <div class="container">
    <AddPlayer on:addplayer={addPlayer}/>
    {#if players.length === 0}
        <p>No players</p>
    {:else}
        {#each players as player}
        <Player name={player.name} points={player.points} />
        {/each}
    {/if}
    </div>
</main>
