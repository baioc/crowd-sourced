// React
import React from 'react';

// Pages
import Home from './pages/Home';
import Options from './pages/Options';
import Label from './pages/Label';
import Select from './pages/Select';

const routes = [
  {
    path: '/',
    element: <Home />,
    children: [
    ]
  },
  {
    path: '/options',
    element: <Options />,
    children: [
    ]
  },
  {
    path: '/label',
    element: <Label />,
    children: [
    ]
  },
  {
    path: '/select',
    element: <Select />,
    children: [
    ]
  },  
];

export default routes;
