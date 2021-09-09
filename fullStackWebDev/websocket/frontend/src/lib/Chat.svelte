<script lang="ts">
  //stores
  import { messageStore } from "../store/msg";
  //ECMA imports
  import { io } from "socket.io-client";
  import { onMount } from "svelte";
  //socket-client init
  let socket;
  onMount(() => {
    socket = io("http://localhost:3100/chat", {
      secure: false,
      reconnect: true,
      rejectUnauthorized: false,
      transports: ["websocket"],
    });
    socket.on("connect", () => {
      console.log("connected");
    });

    socket.on("disconnect", () => {
      console.log("disconnected");
    });

    socket.on("error", console.error);

    socket.on("msgToClient", (msg) => {
      receiveMessage(msg);
    });
  });
  function receiveMessage(msg: string) {
    console.log(`received ${msg}`);
    messageStore.set([...$messageStore, msg]);
  }
  //new msg logic
  let chatMsg: string;
  async function newMsg() {
    if (chatMsg) {
      console.log(`send ${chatMsg}`);
      socket.emit("msgToServer", chatMsg);

      messageStore.set([...$messageStore, chatMsg]);
      console.log($messageStore);
      chatMsg = "";
    }
  }
  const onKeyPress = (e) => {
    if (e.charCode === 13) {
      newMsg();
    }
  };
</script>

<template>
  {$messageStore}
  <div class="flex-grow max-w-screen-md">
    <input
      bind:value={chatMsg}
      on:keypress={onKeyPress}
      type="text"
      name="msg-chat"
      id="msg-chat"
      class="fill-current shadow-sm focus:ring-indigo-500 focus:border-indigo-500 w-full sm:text-sm border-gray-300 rounded-md min-w-max"
      placeholder="Say hello!"
    />
  </div>
</template>
