db.listingAndReviews.createIndex({name: 1});

db.listingAndReviews.find({ name: { $regex: /^Hort*/} }).explain("executionStats")
