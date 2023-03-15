import React, { Component } from 'react';
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    Form,
    FormGroup,
    Input,
    Label
} from 'reactstrap';

class CustomModal extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activeItem: this.props.activeItem
        }
    }

    handleChange = e => {
        let { name, value } = e.target;
        if (e.target.type === 'checkbox') {
            value = e.target.checked;
        }

        const activeItem = { ...this.state.activeItem, [name]: value };
        this.setState({ activeItem });
    }

    render() {
        const { toggle, onSave } = this.props;
        return (
            <Modal isOpen={true} toggle={toggle}>
                <ModalHeader toggle={toggle}>Task Item</ModalHeader>
                <ModalBody>
                    <Form>
                        <FormGroup>
                            <Label htmlFor='author'>Author</Label>
                            <Input
                                type='text'
                                name='author'
                                value={this.state.activeItem.author}
                                onChange={this.handleChange}
                                placeholder='Enter Author'
                            />
                        </FormGroup>

                        <FormGroup>
                            <Label htmlFor='title'>Title</Label>
                            <Input
                                type='text'
                                name='title'
                                value={this.state.activeItem.title}
                                onChange={this.handleChange}
                                placeholder='Enter Title'
                            />
                        </FormGroup>

                        <FormGroup>
                            <Label htmlFor='content'>Content</Label>
                            <Input
                                type='text'
                                name='content'
                                value={this.state.activeItem.content}
                                onChange={this.handleChange}
                                placeholder='Enter Content'
                            />
                        </FormGroup>

                        <FormGroup>
                            <Label htmlFor='birth_date'>Date of Birth</Label>
                            <Input
                                type='date'
                                name='birth_date'
                                value={this.state.activeItem.birth_date}
                                onChange={this.handleChange}
                                placeholder='Enter Birth Date'
                            />
                        </FormGroup>

                        <FormGroup>
                            <Label htmlFor='death_date'>Date of Death</Label>
                            <Input
                                type='date'
                                name='death_date'
                                value={this.state.activeItem.death_date}
                                onChange={this.handleChange}
                                placeholder='Enter Death Date'
                            />
                        </FormGroup>

                        <FormGroup check>
                            <Label htmlFor='is_public'>Is Public</Label>
                            <Input
                                type='checkbox'
                                name='is_public'
                                value={this.state.activeItem.is_public}
                                onChange={this.handleChange}
                            />
                        </FormGroup>
                    </Form>
                </ModalBody>
                <ModalFooter>
                    <Button color='success' onClick={() => onSave(this.state.activeItem)}>
                        Submit
                    </Button>
                </ModalFooter>
            </Modal>
        );
    }
}

export default CustomModal
