
function TestObject(prop) {
    return(
    <h1>Your name is {prop.name} </h1>
    );
}


export default function Page() {
    return(
        <div>
            <h1>You understand react</h1>
            <TestObject name="CHris" />
        </div>
    );
}