import React, { useReducer } from "react";
import { Button, Icon, TextField, Paper, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import ArrowRightAltOutlinedIcon from '@material-ui/icons/ArrowRightAltOutlined';

export function FormSubmit(props) {
    const useStyles = makeStyles(theme => ({
        button: {
            margin: theme.spacing(1)
        },
        leftIcon: {
            marginRight: theme.spacing(1)
        },
        rightIcon: {
            marginLeft: theme.spacing(1)
        },
        iconSmall: {
            fontSize: 20
        },
        root: {
            padding: theme.spacing(2, 1),
            backgroundColor: '#F8F8F8',
        },
        container: {
            display: "flex",
            flexWrap: "wrap"
        },
        textField: {
            marginLeft: theme.spacing(1),
            marginRight: theme.spacing(1),
            width: 400,
            color: '#9CA9B3',
            '&::-webkit-input-placeholder': {
                color: '#9CA9B3'
            },
        },
        form: {
            backgroundColor: '#F8F8F8',
            border: '2px solid #000000',
            boxSizing: 'border-box',
        },
        formName: {
            color: '#9CA9B3',
            display: 'flex',
            fontStyle: 'normal',
            alignItems: 'center',
            fontFamily: 'Roboto',
            fontWeight: 'normal',
        },
    }));

    const [formInput, setFormInput] = useReducer(
        (state, newState) => ({ ...state, ...newState }),
        {
            name: "",
            email: ""
        }
    );

    const handleSubmit = evt => {
        evt.preventDefault();

        let data = { formInput };

        fetch("https://pointy-gauge.glitch.me/api/form", {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(response => response.json())
            .then(response => console.log("Success:", JSON.stringify(response)))
            .catch(error => console.error("Error:", error));
    };

    const handleInput = evt => {
        const name = evt.target.name;
        const newValue = evt.target.value;
        setFormInput({ [name]: newValue });
    };

    const classes = useStyles();

    console.log(props);

    return (
        <div>
            <Paper className={classes.root}>
                <Typography className={classes.formName} variant="h6" component="h6">
                    {props.formName}
                </Typography>
                <Typography className={classes.formName} component="p">{props.formDescription}</Typography>

                <form onSubmit={handleSubmit}>
                    <TextField
                        label="Option"
                        id="outlined-basic"
                        name="name"
                        defaultValue={formInput.email}
                        className={classes.textField}
                        helperText="Enter the option"
                        onChange={handleInput}
                        variant="outlined" 
                    />
                    <Button
                        type="submit"
                        variant="contained"
                        color="primary"
                        className={classes.button}
                    >
                        Submit<ArrowRightAltOutlinedIcon className={classes.rightIcon}>send</ArrowRightAltOutlinedIcon>
                    </Button>
                </form>
            </Paper>
        </div>
    );
}
