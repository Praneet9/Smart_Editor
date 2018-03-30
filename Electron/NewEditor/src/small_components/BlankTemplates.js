import React, { Component } from 'react'

export default class BlankTemplates extends Component {
    

    templateData = () => {
        this.props.getTemplateData("this is template name!!!");
    }
    
    render () {
        return <button onClick={this.templateData}>Template 1</button>
    }
}