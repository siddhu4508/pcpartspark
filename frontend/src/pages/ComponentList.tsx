import React, { useEffect, useState } from 'react';
import client from '../api/client';

interface Component {
    id: number;
    name: string;
    category: string;
    price_inr: number;
}

const ComponentList = () => {
    const [components, setComponents] = useState<Component[]>([]);

    useEffect(() => {
        client.get('/components')
            .then(response => setComponents(response.data))
            .catch(error => console.error(error));
    }, []);
    
    return (
        <div>
            <h2>Component List</h2>
            <ul>
                {components.map(component => (
                    <li key={component.id}>
                        {component.name} - {component.category} - {component.price_inr} INR
                    </li>
                ))}
            </ul>
        </div>
    )
};

export default ComponentList;