import React from 'react'
import { makeStyles } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
    font: {
        fontFamily: 'Roboto',
        fontStyle: 'normal',
        fontWeight: 'normal',
        display: 'flex',
        alignItems: 'center',
        color: '#9CA9B3',
    },
    header: {
        fontSize: '32px',
        lineHeight: '37px',
    },
    body: {
        fontSize: '24px',
        lineHeight: '28px',
    }
}));

export const TextHeader = (({ header, text, linkTo }) => {

    const classes = useStyles();

    return (
        <>
            <p className={`${classes.font} ${classes.header}`}>
                {header}
            </p>
            <p className={`${classes.font} ${classes.body}`}>
                You will be contributing to the dataset
                "<a href={linkTo}>{text}</a>"
            </p>
        </>
    )
});