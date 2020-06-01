import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: []
})
export class FooterComponent implements OnInit {
  year: string;

  constructor() {}

  ngOnInit() {
    this.year = new Date().getFullYear().toString();
  }
}
