<script lang="ts">
    //export let name: string;
    let name: string = "bro McChad";
    let points: number = 100;
    const addPoint = () => {
        points += 1;
    };
    const removePoint = () => {
        points -= 1;
    };
    const showControls: boolean = false
</script>

<style>
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;
    }

    h1 {
        color: #ff3e00;
        text-transform: uppercase;
        font-size: 4em;
        font-weight: 100;
    }

    h3 {
        margin-bottom: 10 px;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
</style>

<main>
    <div class="container">
        <div class="card">
            <h1>{name}</h1>
            <h3>{points}</h3>
            {#if showControls}
                <button class="btn" on:click={addPoint}>+1</button>
                <button class="btn btn-dark" on:click={removePoint}>-1</button>
                <input type="number" bind:value={points} />
            {/if}
        </div>
    </div>
</main>
