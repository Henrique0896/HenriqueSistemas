import React from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';

import Login from './pages/Login';
import Dashboard from './pages/Dashboard';



export default function Routes(){
    return(
        <BrowserRouter>
            <Switch>
                <Route path="/login" exact component={Login} />
                <Route path="/" component={Dashboard} />
            </Switch>
        </BrowserRouter>
    );
}
