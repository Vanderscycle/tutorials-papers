<script lang="ts">//if you do not specify TS, Svelte will assume JS
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher()

    interface PlayerInterface {
        name: string;
        points: number;
    }

    export let player:PlayerInterface = {
        name: '',
        points: 0,
    }

    const onSubmit = (e) => {
        e.preventDefault()
        dispatch("addplayer", player)
        let player = {
        name: '',
        points: 0,
        }
    }
</script>

<form on:submit={onSubmit} class="grid-3">
    <input type="text" placeholder="Player Name" bind:value={player.name}/>
    <input type="number" placeholder="Player Points" bind:value={player.points}/>
    <input type="submit" class="btn btn-primary" value="Add Player"/>
</form>
