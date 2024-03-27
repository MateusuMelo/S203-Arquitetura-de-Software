const express = require('express');
const router = express.Router();
const datafilm_route = require('../services/datafilm_service');

/* GET datafilm_route listing. */
router.get('/', function(req, res, next) {
  try {
    res.json(datafilm_route.getMultiple(req.query.page));
  } catch(err) {
    console.error(`Error while getting quotes `, err.message);
    next(err);
  }
});

module.exports = router;
