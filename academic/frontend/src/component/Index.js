
// import {useEffect, useState} from "react";
// import axios from "axios";
// import {Navigate} from "react-router-dom";

// export const Home = () => {
//     const [message, setMessage] = useState('');

//     useEffect(() => {
//         if(localStorage.getItem('access_token') === null){
//             window.location.href = '/login'  
//         }
//         else{
//             (async () => {
//             try {
//                 const {data} = await axios.get('http://localhost:8000/api/v1/index/', {
//                 headers: {
//                   'Content-Type': 'application/json',
//                 }
//               });

//               setMessage(data.message);
//             } catch (e) {
//                 console.log('not auth')
//             }
//         })()};
//     }, []);



//     return <div className="form-signin mt-5 text-center">
//         <h3>Hi {message}</h3>
        
//     </div>
// }

import { useEffect, useState } from "react";
import axios from "axios";
import { Navigate } from "react-router-dom";

export const Index = () => {
    const [message, setMessage] = useState('');

    useEffect(() => {
        if (localStorage.getItem('access_token') === null) {
            window.location.href = '/login';  
        } else {
            (async () => {
                try {
                    const { data } = await axios.get('http://localhost:8000/api/v1/index/', {
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Bearer ${localStorage.getItem('access_token')}`
                        }
                    });

                    setMessage(data.message);  // Set the message with the user's name
                } catch (e) {
                    console.log('not auth');
                }
            })();
        }
    }, []);  // Run only once when the component mounts

    return (
        <div className="form-signin mt-5 text-center">
            <h3>{message}</h3> {/* Display the "Hi" message with the user's name */}
        </div>
    );
}

