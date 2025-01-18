import { CloseCircleFilled, CloseCircleOutlined, CloseOutlined } from '@ant-design/icons';
import { IconButton, Tab, Tabs } from '@mui/material';
import React, { useCallback, useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router';

const NavTabs = ({ navigation, title }) => {
  const location = useLocation();
  const [activeTabs, setActiveTabs] = useState([]);
  const [activeTab, setActiveTab] = useState(0);
  const navigate = useNavigate();

  useEffect(() => {
    console.log(location);
    if (location.pathname === '/') {
      // TODO navigate to dashboard
      return;
    }
    if (location.state.fromTab) return;

    setActiveTabs([
      ...activeTabs,
      {
        id: activeTabs.length,
        pathname: location.pathname,
        label: location.state ? location.state.item.title : 'Dashboard',
        closeable: location.state ? location.state.item.closeable : false
      }
    ]);
    setActiveTab(activeTabs.length);
  }, [location]);

  const handleClose = useCallback(
    (event, tabToDelete, activeTab) => {
      event.stopPropagation();

      const tabToDeleteIndex = activeTabs.findIndex((tab) => tab.id === tabToDelete.id);

      const updatedTabs = activeTabs.filter((tab, index) => {
        return index !== tabToDeleteIndex;
      });

      console.log(tabToDelete.id, tabToDeleteIndex, activeTab);

      setActiveTabs(updatedTabs);
      if (tabToDelete.id === activeTab) {
        const previousTab = activeTabs[tabToDeleteIndex - 1] || activeTabs[tabToDeleteIndex + 1] || {};
        navigate(previousTab.pathname, {
          state: { item: previousTab, fromTab: true }
        });
        setActiveTab(previousTab.id);
      }
    },
    [activeTabs]
  );

  const handleClick = useCallback((event, tabToActive) => {
    navigate(tabToActive.pathname, {
      state: { item: tabToActive, fromTab: true }
    });
    setActiveTab(tabToActive.id);
  }, []);

  return (
    <>
      <div>tabs: {JSON.stringify(activeTabs)}</div>
      <div>activeTabId: {activeTab}</div>
      <div>
        <Tabs value={activeTab} onChange={(event) => {}}>
          {activeTabs.map((tab) => (
            <Tab
              key={tab.id}
              label={
                typeof tab.label === 'string' ? (
                  <span>
                    {tab.label}
                    {tab.closeable && (
                      <IconButton component="div" onClick={(event) => handleClose(event, tab, activeTab)}>
                        <CloseOutlined />
                      </IconButton>
                    )}
                  </span>
                ) : (
                  tab.label
                )
              }
              onClick={(event) => {
                handleClick(event, tab);
              }}
            />
          ))}
        </Tabs>
      </div>
    </>
  );
};

export default NavTabs;
