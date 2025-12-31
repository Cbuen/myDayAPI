'use client'
import { HOVER_SIMPLE } from "../_utils/anchors/hover";
import { LoginButton } from "../_components/my-buttons";
import { useState } from "react";
import { loginUser, signupUser } from "../_utils/anchors/api";


export default function Page() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    function handleLogin() {
        if (username == "" || password == "") {
            return console.log("BLANK USERNAME OR PASSWORD");
            
        }
        else {
            sessionStorage.setItem("username", username);
            loginUser({"username": username, "password": password});
        }
        
        
    }
    
    return (
        <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
            <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
                <div className="flex flex-col gap-5">
                    <h1>Login Page</h1>
                    <div className="flex flex-col gap-10">
                        <input className="bg-white text-black" type="username" name="username" id="username" placeholder="username" value={username} onChange={(e) => {setUsername(e.target.value)}} />
                        <input className="bg-white text-black" type="text" name="password" id="password" placeholder="password" value={password} onChange={(e) => {setPassword(e.target.value)}} />
                        <LoginButton onClick={handleLogin} />

                        <div className="flex flex-row gap-15">
                            <a className={`${HOVER_SIMPLE}`} href="">Dont have an account?</a>
                            <a className={`${HOVER_SIMPLE}`} href="">Forgot Password?</a>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    );
}
