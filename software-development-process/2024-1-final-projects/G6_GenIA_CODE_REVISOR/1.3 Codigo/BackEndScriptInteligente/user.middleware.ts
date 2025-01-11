import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';
import { PrismaService } from './prisma/prisma.service';

@Injectable()
export class UserMiddleware implements NestMiddleware {
  constructor(private prisma: PrismaService) {}

  async use(req: Request, res: Response, next: NextFunction) {
    const userId = req.headers['user-id'];
    if (userId) {
      const user = await this.prisma.user.findUnique({
        where: { id: Number(userId) },
      });
      if (user) {
        req['user'] = user;
      }
    }
    next();
  }
}
