import Image from "next/image";
import { AddButton, DelButton } from "./_components/my-buttons";
import { todos } from "./_data/testdata";

function TodoDisplay() {
  const listItems = todos.map(todo =>
    <li className="flex flex-row gap-x-5" key={todo}>{todo} <DelButton /></li>
  );

  return (
    <div>
      <ul className="list-none">
        {listItems}
      </ul>
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
          <input type="text" placeholder="Enter a TODO" />
          <AddButton />
        </div>
      </main>
    </div>
  );
}
