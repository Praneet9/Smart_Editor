import React, { Component } from 'react'
import DragThisDocument from '../small_components/DragThisDocument'
import ShowLables from '../small_components/ShowLables'
import DocumentLayout from "../styled_components/DocumentLayout";


export default class DragAndShowLables extends Component {

    state = {
        imagePreviewUrl : '',
        handle: false
    }

    componentWillMount() {
        this.setState({imagePreviewUrl: this.props.setImagePreivewUrl})
    }

    insideDragAndShow = () => {
        this.setState({handle: true})
    }

    render() {
        let whatToShow = null;
        console.log(this.state.handle)
        if(this.state.handle) {
            whatToShow= ( 
            <ShowLables imageAndCoords={this.state.imagePreviewUrl}/> 
        )
        } else {
            whatToShow = (
            <DragThisDocument 
                setImagePreivewUrl={this.state.imagePreviewUrl}
                insideDragThisDocument={this.insideDragAndShow}  />            
            )
        }

        return (
            <DocumentLayout>
                {whatToShow}
            </DocumentLayout>
        )
        
    }

  
}