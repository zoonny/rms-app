import { format, formatDate } from 'date-fns';

const dateFormat = (date) => {
  if (!date) return '';
  return format(new Date(date), 'yyyy-MM-dd');
};

export default dateFormat;
