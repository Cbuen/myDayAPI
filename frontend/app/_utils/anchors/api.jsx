export const API_BASE = 'http://127.0.0.1:8000/'
/**
 * Hold all api requests direclty tied to mydayAPI
 * TOOD: Need to configure a django route for user creation to only get todos tied to a user
 * 
 */


// gets all TODOS in a fetch requests
export async function getTodoLists() {
    const url = `${API_BASE}todo-list/`;
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status ${response.status}`);
        }
        const result = await response.json();
        console.log(result);
    } catch (error) {
        console.log(error.message);
    }
}

// signup user api
export async function signupUser(data) {
    const url = `${API_BASE}users/signup`;
    try {
        const response = await fetch(url, {method:'POST',
            body: JSON.stringify(data),
            mode: "cors",
            headers: {"Content-Type": "application/json"}
        });
        if (!response.ok) {
            throw new Error(`Response status ${response.status}`);
        }
        const result = await response.json();
        console.log(result);
    } catch (error) {
        console.log(error.message);
    }
}

export async function loginUser(data) {
    const url = `${API_BASE}login/`;
    try {
        const response = await fetch(url, {method: 'POST',
            body: JSON.stringify(data),
            mode: "cors",
            headers: {"Content-type": "application/json"}
        });
        
        if (!response.ok) {
            console.error(data=`${response.status}`);
        }
    }
    catch (error) {
        console.error(data=error.message);
    }
}

