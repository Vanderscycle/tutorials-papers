<script lang="ts">
    //export let name: string;
    //let name: string = "bro McChad";
    //let points: number = 100;
    export let name:string
    export let points:number
    let showControls: boolean = false

    const addPoint = () => {
        points += 1;
    };
    const removePoint = () => {
        points -= 1;
    };
    const toggleControls = ():void => {showControls = !showControls}
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
    <div class="card">
        <h1>
            {name}
            <button class="btn btn-sm" on:click={toggleControls}>
            {#if showControls}-{:else}+{/if}
            </button>

        </h1>
        <h3>points: {points}</h3>
        {#if showControls}
            <button class="btn" on:click={addPoint}>+1</button>
            <button class="btn btn-dark" on:click={removePoint}>-1</button>
            <input type="number" bind:value={points} />
        {/if}
    </div>
</main>

