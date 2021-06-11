import API from '../API/API.js';
require('dotenv').config({ path: '../../safe.env'});

export const getSelect = async () => {
    try {
        return await API.getRequest(`${process.env.REACT_APP_API_URL}/select`);
    } catch (error) {
        throw new Error(`Error encountered while communication with server! Error is "${error.message}"`)
    };
};

export const postSelect = async (__dataBlob) => {
    try {
        return await API.postRequest(`${process.env.REACT_APP_API_URL}/select`, __dataBlob );
    } catch (error) {
        throw new Error(`Error encountered while communication with server! Error is "${error.message}"`)
    };
};