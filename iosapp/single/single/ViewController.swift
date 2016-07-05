//
//  ViewController.swift
//  single
//
//  Created by Jerome Cao on 3/07/16.
//  Copyright © 2016 Jerome Cao. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UITableViewDataSource, UITableViewDelegate, HomeModelProtocal  {
    
    //Properties
    @IBOutlet weak var Listtableview: UITableView!    
    
    var feedItems: NSArray = NSArray()
    var selectedLocation : localmodel = localmodel()
    //@IBOutlet weak var Listtableview: UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //set delegates and initialize homeModel
        
        self.Listtableview.delegate = self
        self.Listtableview.dataSource = self
        
        let homeModel = homemodel()
        homeModel.delegate = self
        homeModel.downloadItems()
        
    }
    
    func itemsDownloaded(items: NSArray) {
        
        feedItems = items
        self.Listtableview.reloadData()
    }
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // Return the number of feed items
        return feedItems.count
        
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        // Retrieve cell
        let cellIdentifier: String = "basiccell"
        let myCell: UITableViewCell = tableView.dequeueReusableCellWithIdentifier(cellIdentifier)!
        // Get the location to be shown
        let item: localmodel = feedItems[indexPath.row] as! localmodel
        // Get references to labels of cell
        myCell.textLabel!.text = item.date
        
        return myCell
    }
    
}


//class ViewController: UIViewController {

//    @IBOutlet weak var listtableview: UITableViewCell!
    
    
//    override func viewDidLoad() {
//        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
//    }


//    override func didReceiveMemoryWarning() {
//        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
//    }


//}

