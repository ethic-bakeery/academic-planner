
import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export const Register = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');
    const [email, setEmail] = useState('');
    const [error, setError] = useState('');
    const [successMessage, setSuccessMessage] = useState('');
    
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        // Check if passwords match
        if (password !== password2) {
            setError("Passwords do not match");
            setSuccessMessage('');
            return;
        }

        // Prepare the data
        const user = {
            username: username,
            password: password,
            email: email,
        };

        try {
            // Send the data to the backend for registration
            const { data } = await axios.post('http://localhost:8000/api/v1/register/', user, {
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            console.log(data);

            // If successful, display success message and redirect to login page
            setSuccessMessage("Registration successful! You can now log in.");
            setError('');
            setTimeout(() => {
                navigate('/login');
            }, 2000);
        } catch (error) {
            console.log("Error during registration:", error);
            setError("An error occurred during registration. Please try again.");
            setSuccessMessage('');
        }
    };

    return (
        <div className="Auth-form-container">
            <form className="Auth-form" onSubmit={handleSubmit}>
                <div className="Auth-form-content">
                    <h3 className="Auth-form-title">Register</h3>

                    {/* Username Field */}
                    <div className="form-group mt-3">
                        <label>Username</label>
                        <input
                            className="form-control mt-1"
                            placeholder="Enter Username"
                            name="username"
                            type="text"
                            value={username}
                            required
                            onChange={(e) => setUsername(e.target.value)}
                        />
                    </div>

                    {/* Email Field */}
                    <div className="form-group mt-3">
                        <label>Email</label>
                        <input
                            className="form-control mt-1"
                            placeholder="Enter Email"
                            name="email"
                            type="email"
                            value={email}
                            required
                            onChange={(e) => setEmail(e.target.value)}
                        />
                    </div>

                    {/* Password Field */}
                    <div className="form-group mt-3">
                        <label>Password</label>
                        <input
                            name="password"
                            type="password"
                            className="form-control mt-1"
                            placeholder="Enter password"
                            value={password}
                            required
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>

                    {/* Confirm Password Field */}
                    <div className="form-group mt-3">
                        <label>Confirm Password</label>
                        <input
                            name="password2"
                            type="password"
                            className="form-control mt-1"
                            placeholder="Confirm password"
                            value={password2}
                            required
                            onChange={(e) => setPassword2(e.target.value)}
                        />
                    </div>

                    {/* Error message */}
                    {error && <div className="alert alert-danger mt-3">{error}</div>}

                    {/* Success message */}
                    {successMessage && <div className="alert alert-success mt-3">{successMessage}</div>}

                    {/* Submit Button */}
                    <div className="d-grid gap-2 mt-3">
                        <button type="submit" className="btn btn-primary">
                            Register
                        </button>
                    </div>
                    <div className="text-center mt-4">
                        <p className="text-sm text-gray-600">
                            Already Registered? <a href="/login" className="text-blue-500 hover:text-blue-600">Login here</a>
                        </p>
                    </div>
                </div>
            </form>
        </div>
    );
};

