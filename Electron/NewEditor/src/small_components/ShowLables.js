import React, { Component } from 'react'

export default class ShowLables extends Component{
    
    state = { 
        imagePreviewUrl: ''
    }

    componentWillMount() {
        this.setState({
            imagePreviewUrl: this.props.imageAndCoords
        })
    }

    

    render () {

        return (
            <img
            src={this.state.imagePreviewUrl}
            alt="logo"
            style={{ width: 450, height: 650, margin: "10px" }}
          />
        )


        
    }
}