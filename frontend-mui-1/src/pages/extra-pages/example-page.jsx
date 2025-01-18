import React, { useState } from 'react';
import { useLocation } from 'react-router';

// Define the menu data
const menuData = [
  {
    title: 'Home',
    items: []
  },
  {
    title: 'About',
    items: [
      {
        title: 'Team',
        items: []
      },
      {
        title: 'Company',
        items: [
          {
            title: 'History',
            items: []
          },
          {
            title: 'Vision',
            items: []
          }
        ]
      }
    ]
  },
  {
    title: 'Services',
    items: [
      {
        title: 'Consulting',
        items: []
      },
      {
        title: 'Development',
        items: []
      }
    ]
  },
  {
    title: 'Contact',
    items: []
  }
];

// MenuItem component
const MenuItem = ({ item, onClick, expandedItems }) => {
  const isExpanded = expandedItems.includes(item.title);

  return (
    <li>
      <div onClick={() => onClick(item.title)}>{item.title}</div>
      {isExpanded && item.items.length > 0 && (
        <ul>
          {item.items.map((subItem) => (
            <MenuItem key={subItem.title} item={subItem} onClick={onClick} expandedItems={expandedItems} />
          ))}
        </ul>
      )}
    </li>
  );
};

// Menu component
const Menu = ({ data }) => {
  const [expandedItems, setExpandedItems] = useState([]);

  const handleClick = (title) => {
    setExpandedItems((prev) => (prev.includes(title) ? prev.filter((item) => item !== title) : [...prev, title]));
  };

  return (
    <ul>
      {data.map((item) => (
        <MenuItem key={item.title} item={item} onClick={handleClick} expandedItems={expandedItems} />
      ))}
    </ul>
  );
};

function ExamplePage(props) {
  const { state } = useLocation();
  return (
    <div>
      <h1>Navigator Menu</h1>
      <Menu data={menuData} />
      <h3>props: {JSON.stringify(props)}</h3>
      <h3>state: {JSON.stringify(state)}</h3>
    </div>
  );
}

export default ExamplePage;
