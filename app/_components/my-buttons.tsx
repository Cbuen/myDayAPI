const BORDER_RADIUS = "rounded-lg";

export function AddButton() {
    return (
        <button className={`bg-green-400 ${BORDER_RADIUS}`}>
            Add
        </button>
    );
}

export function DelButton() {
    return (
        <button className={`bg-red-400 ${BORDER_RADIUS} w-[5vw]`}>
            DEL
        </button>
    );
}

export function LoginButton() {
    return (
        <button className={`bg-green-600 w-full ${BORDER_RADIUS}`}>
            Sign in
        </button>
    );
}

export function Signup({onClick}: { onClick: () => void}) {
    return (
        <button onClick={onClick} className={`bg-green-600 w-full ${BORDER_RADIUS}`}>
            Signup
        </button>
    );
}