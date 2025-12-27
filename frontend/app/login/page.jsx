import { HOVER_SIMPLE } from "../_utils/anchors/hover";
import { LoginButton } from "../_components/my-buttons";

export default function Page() {
    return (
        <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
            <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
                <div className="flex flex-col gap-5">
                    <h1>Login Page</h1>
                    <div className="flex flex-col gap-10">
                        <input className="bg-white text-black" type="email" name="email" id="email" placeholder="email" />
                        <input className="bg-white text-black" type="text" name="password" id="password" placeholder="password" />
                        <LoginButton />

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