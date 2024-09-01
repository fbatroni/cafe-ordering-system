const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());

app.get('/api', (req, res) => {
  res.json({ message: 'This is the API endpoint' });
});
const PORT = process.env.PORT || 8001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
