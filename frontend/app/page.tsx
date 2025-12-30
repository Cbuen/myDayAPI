"use client"
import Image from "next/image";
import { AddButton, DelButton } from "./_components/my-buttons";
import { useState } from "react";





/**
 * TODO:
 * Refreactor be its own component 
 */
function TodoDisplay() {
  const [inputValue, setInputValue] = useState("");

  //TODO: later refractor for db linking
  const [todos, setTodo] = useState(['Walk the dog', 'Go for run']);

  const listItems = todos.map(t =>
    <li className="flex flex-row gap-x-5" key={t}>{t} <DelButton /></li>
  );

  return (
    <div className="flex flex-col gap-y-2.5">
      <ul className="list-none">
        {listItems}
      </ul>
      <input onChange={(e) => {
        setInputValue(e.target.value);
      }} value={inputValue} type="text" placeholder="Enter a TODO" />
      <AddButton onClick={() => {
        console.log("Add Button Click");
        if (inputValue == "") return;

        const newTodos = [...todos, inputValue];
        setTodo(newTodos);
        setInputValue("");
      }} />
    </div>

  );
}




export default function Home() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
        <div className="flex flex-col gap-5">
          <h1>Landing Page</h1>
          <TodoDisplay />

        </div>
      </main>
    </div>
  );
}
