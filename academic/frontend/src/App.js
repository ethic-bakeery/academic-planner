import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import {Login} from "./component/Login";
import {Index} from "./component/Index";
import {Navigation} from './component/navigation';
import {Logout} from './component/Logout';
import {Register} from './component/Register';

function App() {
    return <BrowserRouter>
    <Navigation></Navigation>
        <Routes>
            <Route path="/" element={<Index/>}/>
            <Route path="/login" element={<Login/>}/>
            <Route path="/logout" element={<Logout/>}/>
	    <Route path="/register" element={<Register/>}/>

        </Routes>
    </BrowserRouter>;
}

export default App;
