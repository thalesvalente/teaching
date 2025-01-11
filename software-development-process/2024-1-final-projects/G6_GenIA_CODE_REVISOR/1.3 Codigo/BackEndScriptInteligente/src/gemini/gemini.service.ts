// import { Injectable, HttpService } from '@nestjs/common';
// import { ConfigService } from '@nestjs/config';
// import { Observable } from 'rxjs';
// import { map } from 'rxjs/operators';

// @Injectable()
// export class GeminiService {
//   private apiUrl: string;

//   constructor(
//     private httpService: HttpService,
//     private configService: ConfigService,
//   ) {
//     this.apiUrl = this.configService.get<string>('GEMINI_API_URL');
//   }

//   getGeminiData(endpoint: string): Observable<any> {
//     return this.httpService
//       .get(`${this.apiUrl}/${endpoint}`)
//       .pipe(map((response) => response.data));
//   }
// }
