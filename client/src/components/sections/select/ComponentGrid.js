import React from 'react';
import { Grid, Button, makeStyles } from '@material-ui/core';

// Local imports
import { TextHeader } from '../TextHeader';
import { ImageGrid } from './ImageGrid';

const useStyles = makeStyles((theme) => ({
    root: {
        '& > *': {
            margin: theme.spacing(1),
        },
    },
}));

export const ComponentGrid = (() => {

    const classes = useStyles();

    return (
        <div className={classes.root}>
            <Grid container
                direction="column"
                justify="center"
                alignItems="center"
                spacing={2}
            >
                <Grid item xs={12}>
                    <TextHeader header={'Please select images that contain \'Cars\''} text={'Computer Vision for autonomous driving'} linkTo={'http://kaggle.com/'} />
                </Grid>
                <Grid item xs={12}>
                    <ImageGrid />
                </Grid>
                <Grid item xs={12}>
                    <Button variant="contained">Submit!</Button>
                </Grid>
            </Grid>
        </div>
    );
});