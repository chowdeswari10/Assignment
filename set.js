db.zips.aggregate([{
      $project: {
      roundedField: { $round: ["$pop", 2] }
    }
    }])
