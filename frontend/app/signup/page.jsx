'use client'; // Marks this component and its imports as client-side code
import { HOVER_SIMPLE } from "../_utils/anchors/hover";
import { Signup } from "../_components/my-buttons";
import { useState } from "react";
import { getTodoLists, signupUser } from "../_utils/anchors/api";




function SignupDetails() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    function handleSignup() {
        if (username == "" || password == "") {
            return console.log("BLANK USERNAME OR PASSWORD");
            
        }
        else {
            console.log(username);
            console.log(password);
            signupUser({"username": username, "password": password})
        }
        
        
    }

    return (
        <div className="flex flex-col gap-y-5">
            <input
                placeholder="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="bg-white text-black"
            />
            <input
                placeholder="password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="bg-white text-black"
            />
            <Signup onClick={handleSignup}/>
            <a className={`${HOVER_SIMPLE}`} href="">Have account? Please login!</a>

        </div>
    );
}

export default function Page() {
    return (
        <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
            <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
                <div className="flex flex-col gap-5">
                    <h1>Signup Page</h1>
                    <SignupDetails />
                </div>
            </main>
        </div>
    );
}