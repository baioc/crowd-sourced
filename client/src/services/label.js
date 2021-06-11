import API from '../API/API.js';
require('dotenv').config({ path: '../../safe.env'});

export const getLabels = async () => {
    try {
        return await API.getRequest(`${process.env.REACT_APP_API_URL}/labels`);
    } catch (error) {
        throw new Error(`Error encountered while communication with server! Error is "${error.message}"`)
    };
};

export const postLabels = async (__dataBlob) => {
    try {
        return await API.postRequest(`${process.env.REACT_APP_API_URL}/labels`, __dataBlob );
    } catch (error) {
        throw new Error(`Error encountered while communication with server! Error is "${error.message}"`)
    };
};