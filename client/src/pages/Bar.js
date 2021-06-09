import { makeStyles } from '@material-ui/core';
import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles((theme) => ({
    appbar: {
        background: '#292929',
    },
    font: {
        flexGrow: 1,
        fontFamily: 'Roboto',
        fontStyle: 'normal',
        fontWeight: 'normal',
        fontSize: '20px',
        lineHeight: '37px',
        /* identical to box height */
        
        display: 'flex',
        alignItems: 'center',
        
        color: '#FFFFFF',        
    }    
}));

export default function Bar({ content }) {
    const classes = useStyles();

    return (
        <AppBar className={classes.appbar} position="static">
            <Toolbar>
                <Typography variant="h6" className={classes.font}>
                    {content}
                </Typography>
            </Toolbar>
        </AppBar>
    );
};