import React, { useState, useCallback, useEffect } from 'react';
import { IconButton, Tab, Tabs } from '@mui/material';
import { CloseCircleFilled } from '@ant-design/icons';
import SamplePage from 'pages/extra-pages/sample-page';

const NavTabs = ({ tabs, selectedTab = 1, onClose, ...rest }) => {
  const [activeTab, setActiveTab] = useState(selectedTab);
  const [activetabs, setActiveTabs] = useState([]);

  useEffect(() => {
    setActiveTabs(tabs);
  }, [tabs]);

  const handleChange = useCallback((event, activeTab) => {
    setActiveTab(activeTab);
  }, []);

  const handleClose = useCallback(
    (event, tabToDelete) => {
      event.stopPropagation();

      const tabToDeleteIndex = activetabs.findIndex((tab) => tab.id === tabToDelete.id);
      const updatedTabs = activetabs.filter((tab, index) => {
        return index !== tabToDeleteIndex;
      });
      onClose(tabToDeleteIndex);
      const previousTab = activetabs[tabToDeleteIndex - 1] || activetabs[tabToDeleteIndex + 1] || {};
      setActiveTabs(updatedTabs);
      setActiveTab(previousTab.id);
    },
    [activetabs]
  );

  return (
    <>
      <div>{JSON.stringify(activetabs)}</div>
      <div>
        <Tabs value={activeTab} onChange={handleChange}>
          {activetabs.map((tab) => (
            <Tab
              key={tab.id}
              value={tab.id}
              label={
                typeof tab.label === 'string' ? (
                  <span>
                    {tab.label}
                    {tab.closeable && (
                      <IconButton component="div" onClick={(event) => handleClose(event, tab)}>
                        <CloseCircleFilled />
                      </IconButton>
                    )}
                  </span>
                ) : (
                  tab.label
                )
              }
            />
          ))}
        </Tabs>
        {/* {activetabs.map((tab) => (activeTab === tab.id ? <TabContainer key={tab.id}>{tab.component}</TabContainer> : null))} */}
      </div>
    </>
  );
};
export default NavTabs;
