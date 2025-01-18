import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { Box, Stack } from '@mui/material';
import { RichTreeView } from '@mui/x-tree-view';
import { List, ListItem, ListItemText, Collapse } from '@mui/material';
import { DownOutlined, HomeOutlined, LoginOutlined, StarOutlined, StarTwoTone, ToolOutlined, UpOutlined } from '@ant-design/icons';
import { useNavigate } from 'react-router';
import menuData from './MenuData';
// import { ExpandLess, ExpandMore } from '@mui/icons-material';

function findObjectsInArray(arr, key, value) {
  let result = [];

  function search(array) {
    for (const item of array) {
      if (item[key] === value) {
        result.push(item);
      }
      for (const k in item) {
        if (typeof item[k] === 'object' && item[k] !== null) {
          if (Array.isArray(item[k])) {
            search(item[k]);
          } else {
            search([item[k]]);
          }
        }
      }
    }
  }

  search(arr);
  return result;
}

// MenuItem component
const MenuItem = ({ item, onClick, expandedItems, activeItem }) => {
  const isExpanded = expandedItems.includes(item.title);
  const paddingLeft = useMemo(() => item.depth + 1, []);
  const isActive = activeItem?.title === item.title;

  return (
    <>
      <ListItem
        button
        onClick={() => onClick(item)}
        sx={isActive ? { color: 'primary.light', fontWeight: 'bold' } : { color: 'text.primary' }}
      >
        {item.icon}
        <ListItemText primary={item.title} sx={{ paddingLeft: paddingLeft }} />
        {item.items.length > 0 ? isExpanded ? <UpOutlined /> : <DownOutlined /> : null}
      </ListItem>
      {item.items.length > 0 && (
        <Collapse in={isExpanded} timeout="auto" unmountOnExit>
          <List component="div" disablePadding>
            {item.items.map((subItem) => (
              <MenuItem key={subItem.title} item={subItem} onClick={onClick} expandedItems={expandedItems} activeItem={activeItem} />
            ))}
          </List>
        </Collapse>
      )}
    </>
  );
};

// Menu component
const Menu = ({ data }) => {
  const [expandedItems, setExpandedItems] = useState([]);
  const [activeItem, setActiveItem] = useState(undefined);
  const navigate = useNavigate();

  useEffect(() => {
    const item = findObjectsInArray(data, 'title', 'Dashboard');
    setActiveItem(Array.isArray(item) ? item[0] : item);
    setExpandedItems(['Navigation']);
  }, []);

  const handleClick = useCallback((item) => {
    setExpandedItems((prev) => (prev.includes(item.title) ? prev.filter((i) => i !== item.title) : [...prev, item.title]));
    if (item.path) {
      navigate(item.path, { state: { item: item } });
      setActiveItem(item);
    }
  }, []);

  return (
    <>
      {/* <div>{JSON.stringify(activeItem)}</div> */}
      <List>
        {data.map((item) => (
          <MenuItem key={item.title} item={item} onClick={handleClick} expandedItems={expandedItems} activeItem={activeItem} />
        ))}
      </List>
    </>
  );
};

function NavigationMenu() {
  return (
    <Box sx={{ minHeight: 352, minWidth: 250 }}>
      <Menu data={menuData} />
    </Box>
  );
}

export default NavigationMenu;
